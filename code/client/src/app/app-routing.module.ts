import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainMenuComponent }    from './main-menu/main-menu.component';
import { DataListComponent }    from './data-list/data-list.component';
import { DataDetailComponent }  from './data-detail/data-detail.component';
import { ContactComponent }     from './contact/contact.component';

const routes: Routes = [
  { path: '', redirectTo: '/main-menu', pathMatch: 'full' },
  { path: 'main-menu', component: MainMenuComponent },
  { path: 'detail/:id', component: DataDetailComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'data-list', component: DataListComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
