declare var initBubbleViz: any;


import { Component, OnInit } from '@angular/core';
import "../../assets/script/tableau-initBubbleViz.js";

@Component({
  selector: 'app-bubble',
  templateUrl: './bubble.component.html',
  styleUrls: ['./bubble.component.css']
})
export class BubbleComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {

    new initBubbleViz();
  
    }

}
