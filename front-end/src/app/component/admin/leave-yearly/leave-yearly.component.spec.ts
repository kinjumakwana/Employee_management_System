import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LeaveYearlyComponent } from './leave-yearly.component';

describe('LeaveYearlyComponent', () => {
  let component: LeaveYearlyComponent;
  let fixture: ComponentFixture<LeaveYearlyComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LeaveYearlyComponent]
    });
    fixture = TestBed.createComponent(LeaveYearlyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
