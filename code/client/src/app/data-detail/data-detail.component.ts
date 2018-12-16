import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Chart } from 'chart.js'

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
    chart = [];
    barChart = [];

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
          .subscribe(data => {
              this.data = data

              let value  = data['list'].map(res => res.value)
              let dates  = data['list'].map(res => res.date)

              this.chart = new Chart('canvas', {
                  type: 'line',
                  data: {
                      labels: dates,
                      datasets: [
                          {
                              data: value,
                              borderColor: '#3cba9f',
                              fill: false
                          }
                      ]
                  },
                  options: {
                      layout: {
                        padding: {
                            left: 25,
                            right: 25,
                            top: 25,
                            bottom: 25
                        }
                      },
                      legend: {
                          display: false
                      },
                      scales: {
                          xAxes: [{
                              display: true
                          }],
                          yAxes: [{
                              display: true
                          }]
                      }
                  }
              })

              this.barChart = new Chart('barCanvas', {
                  type: 'bar',
                  data: {
                      labels: dates,
                      datasets: [
                          {
                              data: value,
                              borderColor: '#3cba9f',
                              fill: false
                          }
                      ]
                  },
                  options: {
                      layout: {
                        padding: {
                            left: 25,
                            right: 25,
                            top: 25,
                            bottom: 25
                        }
                      },
                      legend: {
                          display: false
                      },
                      scales: {
                          xAxes: [{
                              display: true
                          }],
                          yAxes: [{
                              display: true
                          }]
                      }
                  }
              })
          });
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
