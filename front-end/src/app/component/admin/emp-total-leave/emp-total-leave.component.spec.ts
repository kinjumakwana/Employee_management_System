import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmpTotalLeaveComponent } from './emp-total-leave.component';

describe('EmpTotalLeaveComponent', () => {
  let component: EmpTotalLeaveComponent;
  let fixture: ComponentFixture<EmpTotalLeaveComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EmpTotalLeaveComponent]
    });
    fixture = TestBed.createComponent(EmpTotalLeaveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
