import { Routes } from '@angular/router';
import { NgbdpaginationBasicComponent } from './pagination/pagination.component';
import { TableComponent } from './table/table.component';
import { EmployeesComponent } from './admin/employees/employees.component';
import { HolidaysComponent } from './admin/holidays/holidays.component';
import { LeaveComponent } from './admin/leave/leave.component';
import { AttendanceComponent } from './admin/attendance/attendance.component';
import { PayrollComponent } from './admin/payroll/payroll.component';
import { LeaveYearlyComponent } from './admin/leave-yearly/leave-yearly.component';
import { EmpTotalLeaveComponent } from './admin/emp-total-leave/emp-total-leave.component';


export const ComponentsRoutes: Routes = [
	{
		path: '',
		children: [
			{
				path: 'table',
				component: TableComponent
			},
			
			{
				path: 'admin/employees',
				component: EmployeesComponent
			},
			{
				path: 'admin/holidays',
				component: HolidaysComponent
			},
			{
				path: 'admin/leave',
				component: LeaveComponent
			},
			{
				path: 'admin/attendance',
				component: AttendanceComponent
			},
			{
				path: 'admin/payroll',
				component: PayrollComponent
			},
			{
				path: 'admin/leave-yearly',
				component: LeaveYearlyComponent
			},
			{
				path: 'admin/emp-total-leave',
				component: EmpTotalLeaveComponent
			},
			
		]
	}
];
