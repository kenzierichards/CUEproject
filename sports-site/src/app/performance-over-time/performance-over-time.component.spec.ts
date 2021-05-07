import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerformanceOverTimeComponent } from './performance-over-time.component';

describe('PerformanceOverTimeComponent', () => {
  let component: PerformanceOverTimeComponent;
  let fixture: ComponentFixture<PerformanceOverTimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PerformanceOverTimeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PerformanceOverTimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
