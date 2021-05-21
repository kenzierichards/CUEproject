declare var initAthleteViz: any; //holds visualization

import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initAthleteViz.js"; //script 

@Component({
  selector: 'app-athletes-page',
  templateUrl: './athletes-page.component.html',
  styleUrls: ['./athletes-page.component.css']
})
export class AthletesPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {
  //loads visualization from script after view initialized
    new initAthleteViz();
  
    }

}
