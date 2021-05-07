declare var initPOTBarViz: any;

import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initPOTBarViz.js";

@Component({
  selector: 'app-performance-over-time-bar',
  templateUrl: './performance-over-time-bar.component.html',
  styleUrls: ['./performance-over-time-bar.component.css']
})
export class PerformanceOverTimeBarComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {

    new initPOTBarViz();
  
    }

}
