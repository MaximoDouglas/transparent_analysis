import { Component, OnInit } from '@angular/core';

import { Data } from '../data';
import { DataService } from '../data.service';

@Component({
  selector: 'app-data-list',
  templateUrl: './data-list.component.html',
  styleUrls: ['./data-list.component.css']
})
export class DataListComponent implements OnInit {

    data_list: Data[];
    isLoading: boolean;

    constructor(private dataService: DataService) { }

    ngOnInit() {
      this.isLoading = false;
      this.getDataList();
    }

    getDataList(): void {
      this.dataService.getDataList()
      .subscribe(data_list => this.data_list = data_list);
    }

    get(state: number,beginYear: number,endYear: number): void {

      this.isLoading = true;

      if (!state || !beginYear || !endYear) { return; }

      this.dataService.get(state,beginYear,endYear).subscribe( () => {
          this.ngOnInit();
      });
    }

    delete(data: Data): void {
      this.data_list = this.data_list.filter(d => d !== data);
      this.dataService.deleteData(data).subscribe();
    }

}
