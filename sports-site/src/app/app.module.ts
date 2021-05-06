import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from './home/home.component';
import { InfocardsComponent } from './infocards/infocards.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FooterComponent } from './footer/footer.component';
import { AthletesPageComponent } from './athletes-page/athletes-page.component';
import { MeetsPageComponent } from './meets-page/meets-page.component';
import { BubbleComponent } from './bubble/bubble.component';
import { PerformanceOverTimeComponent } from './performance-over-time/performance-over-time.component';
import { PerformanceOverTimeBarComponent } from './performance-over-time-bar/performance-over-time-bar.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    InfocardsComponent,
    routingComponents,
    FooterComponent,
    AthletesPageComponent,
    MeetsPageComponent,
    BubbleComponent,
    PerformanceOverTimeComponent,
    PerformanceOverTimeBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
