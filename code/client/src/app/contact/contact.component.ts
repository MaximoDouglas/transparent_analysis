import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

import { Message } from '../message';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
    message: Message;

    constructor(private dataService: DataService) { }

    ngOnInit() {
    }

    send(name: string,content: string): void {

        this.message = new Message();
        this.message.name = name.trim();
        this.message.content = content.trim();

        if (!name || !content) { return; }

        this.dataService.postMessage(this.message).subscribe( msg => this.message = msg );

  }

}
