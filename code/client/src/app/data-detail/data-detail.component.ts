import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Data }         from '../data';
import { DataService }  from '../data.service';

@Component({
  selector: 'app-data-detail',
  templateUrl: './data-detail.component.html',
  styleUrls: ['./data-detail.component.css']
})
export class DataDetailComponent implements OnInit {

    data: Data;
    id: string;

    constructor(
        private route: ActivatedRoute,
        private dataService: DataService,
        private location: Location
    ) {}

    ngOnInit(): void {
        this.getData();
    }

    getData(): void {
        const id = String(this.route.snapshot.paramMap.get('id'));
        this.id = id;
        
        this.dataService.getData(id)
          .subscribe(data => this.data = data);
    }

    goBack(): void {
        this.location.back();
    }

    save(): void {
        this.data.id = this.id + '#' + this.data.id;

        this.dataService.updateData(this.data)
          .subscribe(() => this.goBack());
    }

}
