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

    constructor(private dataService: DataService) { }

    ngOnInit() {
      console.log("Ola");
      this.getDataList();
    }

    getDataList(): void {
      this.dataService.getDataList()
      .subscribe(data_list => this.data_list = data_list);
    }

    /**
    add(name: string): void {
      name = name.trim();
      if (!name) { return; }
      this.heroService.addHero({ name } as Hero)
        .subscribe(hero => {
          this.heroes.push(hero);
        });
    }
    */

    delete(data: Data): void {
      this.data_list = this.data_list.filter(d => d !== data);
      this.dataService.deleteData(data).subscribe();
    }

}
