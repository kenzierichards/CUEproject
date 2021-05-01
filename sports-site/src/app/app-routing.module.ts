import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { HomeComponent } from './home/home.component';
import { MeetsPageComponent } from './meets-page/meets-page.component';
import { AthletesPageComponent } from './athletes-page/athletes-page.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  { 
    path: 'about', 
    component: AboutComponent
  },
  {
    path: 'athletes',
    component: AthletesPageComponent
  },
  {
    path: 'meets',
    component: MeetsPageComponent
  },
  {
    path: '**',
    redirectTo: '/home',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [AboutComponent]