import { CUSTOM_ELEMENTS_SCHEMA,NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ComponentsRoutes } from './component.routing';
import { NgbdpaginationBasicComponent } from './pagination/pagination.component';
import { TableComponent } from "./table/table.component";
import { AdminComponent } from './admin/admin.component';
import { EmployeesComponent } from './admin/employees/employees.component';
import { HolidaysComponent } from './admin/holidays/holidays.component';
import { LeaveComponent } from './admin/leave/leave.component';
import { AttendanceComponent } from './admin/attendance/attendance.component';
import { PayrollComponent } from './admin/payroll/payroll.component';
import { LeaveYearlyComponent } from './admin/leave-yearly/leave-yearly.component';
import { EmpTotalLeaveComponent } from './admin/emp-total-leave/emp-total-leave.component';
import {MatTableModule} from '@angular/material/table';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatInputModule} from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import {MatSortModule} from '@angular/material/sort';



@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(ComponentsRoutes),
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
    NgbdpaginationBasicComponent,
    TableComponent,
    MatTableModule,
    MatPaginatorModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatProgressSpinnerModule,
    FormsModule,
    HttpClientModule,
    
  ],
  declarations: [
    AdminComponent,
    EmployeesComponent,
    HolidaysComponent,
    LeaveComponent,
    AttendanceComponent,
    PayrollComponent,
    LeaveYearlyComponent,
    EmpTotalLeaveComponent
  ],
  exports: [
    MatTableModule,
    MatSortModule,
    MatProgressSpinnerModule,
    MatInputModule,
    MatPaginatorModule,
    
   
  ],
})
export class ComponentsModule { }
