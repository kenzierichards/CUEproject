declare var initPOTViz: any;

import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initPOTViz.js";

@Component({
  selector: 'app-performance-over-time',
  templateUrl: './performance-over-time.component.html',
  styleUrls: ['./performance-over-time.component.css']
})
export class PerformanceOverTimeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {

    new initPOTViz();
  
    }


}
