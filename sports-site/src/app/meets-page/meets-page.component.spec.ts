import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeetsPageComponent } from './meets-page.component';

describe('MeetsPageComponent', () => {
  let component: MeetsPageComponent;
  let fixture: ComponentFixture<MeetsPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MeetsPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MeetsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
