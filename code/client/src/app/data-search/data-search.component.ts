import { Component, OnInit }    from '@angular/core';
import { Observable, Subject }  from 'rxjs';

import { Data }                 from '../data';
import { DataService }          from '../data.service';

import {
   debounceTime, distinctUntilChanged, switchMap
 } from 'rxjs/operators';

@Component({
  selector: 'app-data-search',
  templateUrl: './data-search.component.html',
  styleUrls: ['./data-search.component.css']
})
export class DataSearchComponent implements OnInit {
    data_list$: Observable<Data[]>;
    private searchTerms = new Subject<string>();

    constructor(private dataService: DataService) {}

    // Push a search term into the observable stream.
    search(term: string): void {
      this.searchTerms.next(term);
    }

    ngOnInit(): void {
      this.data_list$ = this.searchTerms.pipe(

        // wait 300ms after each keystroke before considering the term
        debounceTime(300),

        // ignore new term if same as previous term
        distinctUntilChanged(),

        // switch to new search observable each time the term changes
        switchMap((term: string) => this.dataService.searchData(term))
      );
    }
}
