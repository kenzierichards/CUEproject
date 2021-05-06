declare var initAthleteViz: any;

import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initAthleteViz.js";

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

    new initAthleteViz();
  
    }

}
