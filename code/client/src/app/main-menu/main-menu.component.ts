import { Component, OnInit } from '@angular/core';
import { Link } from '../link';

@Component({
  selector: 'app-main-menu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.css']
})
export class MainMenuComponent implements OnInit {

    links: Link[];

    constructor() { }

    ngOnInit() {
        this.links = [
            new Link('API - IBGE','https://servicodados.ibge.gov.br/api/docs'),
            new Link('API - Transparência','http://www.portaltransparencia.gov.br/api-de-dados'),
            new Link('Códigos do Estados','http://www.lgncontabil.com.br/icms/Tabela-Codigo-de-UF-do-IBGE.pdf'),
            new Link('GitHub - Douglas','https://github.com/MaximoDouglas'),
        ];
    }

}
