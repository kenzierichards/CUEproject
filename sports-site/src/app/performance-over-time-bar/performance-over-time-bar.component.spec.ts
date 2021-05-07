import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerformanceOverTimeBarComponent } from './performance-over-time-bar.component';

describe('PerformanceOverTimeBarComponent', () => {
  let component: PerformanceOverTimeBarComponent;
  let fixture: ComponentFixture<PerformanceOverTimeBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PerformanceOverTimeBarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PerformanceOverTimeBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
