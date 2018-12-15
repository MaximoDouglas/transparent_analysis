import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

//import { MainComponent }        from './main/main.component';
import { DataListComponent }    from './data-list/data-list.component';
//import { DataDetailComponent }  from './data-detail/data-detail.component';
/**
const routes: Routes = [
  { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'main', component: MainComponent },
  { path: 'detail/:id', component: DataDetailComponent },
  { path: 'data-list', component: DataListComponent }
];
*/

const routes: Routes = [
  { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'data-list', component: DataListComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
