declare var initMeetViz: any;

import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initMeetViz.js";

@Component({
  selector: 'app-meets-page',
  templateUrl: './meets-page.component.html',
  styleUrls: ['./meets-page.component.css']
})

export class MeetsPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {

    new initMeetViz();
  
    }

}
