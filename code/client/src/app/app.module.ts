import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }    from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DataListComponent } from './data-list/data-list.component';
import { MainMenuComponent } from './main-menu/main-menu.component';
import { DataSearchComponent } from './data-search/data-search.component';
import { DataDetailComponent } from './data-detail/data-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    DataListComponent,
    MainMenuComponent,
    DataSearchComponent,
    DataDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
