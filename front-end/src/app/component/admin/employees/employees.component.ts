import { AfterViewInit, Component, ViewChild,  EventEmitter, Output} from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatSort, Sort, MatSortModule} from '@angular/material/sort';
import { Subject } from 'rxjs';
import { EmpdataserviceService } from '../employees/empdataservice.service'
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.scss']
})

export class EmployeesComponent{
  employees: any[] = [];
  displayedColumns: string[] = [];
  newEmployee: any = {};
  emp_data!: MatTableDataSource<any>;
  dataSource = new MatTableDataSource<any>([]);
  searchValue!: string;


  constructor(private employeeService: EmpdataserviceService,private _liveAnnouncer: LiveAnnouncer) { }

  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

 
  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }
  ngOnInit(): void {
    
    this.dataSource.sort = this.sort;
    this.getEmployees();

  }

  getEmployees(): void {
    this.employeeService.getEmployees().subscribe(
      response => {
        this.emp_data = new MatTableDataSource(response.data);
        console.log(this.emp_data)
        console.log(response.data)

        // Extract field names from filteredData
        if (this.emp_data.filteredData.length > 0) {
          this.displayedColumns = Object.keys(this.emp_data.filteredData[0]);
          console.log(this.displayedColumns)
          
        } else {
          this.displayedColumns = ['Id', 'Gender', 'Mobile_no', 'Designation', 'Department', 'Address', 'Date_of_birth', 'Education', 'Profile_pic', 'Document', 'created_at', 'user','Action'];
        }

         // Add the "actions" column to the displayedColumns array
        this.displayedColumns.push('edit');
        this.displayedColumns.push('delete');

        // this.employees = response.data;
        this.dataSource = new MatTableDataSource<any>(this.emp_data.filteredData);
        this.dataSource.filter = '';
        this.dataSource.connect();
      },
      error => {
        console.log('Error:', error);
      }
    );
  }

  addEmployee(employee: any): void {
    this.employeeService.addEmployee(employee).subscribe(
      response => {
        console.log('New employee added:', response);
        // Refresh the employee list or perform any other necessary actions
        this.getEmployees(); // Refresh the employee list after adding a new employee
        this.newEmployee = {};
      },
      error => {
        console.log('Error:', error);
      }
    );
  }

  getEmployeeDetails(id: number): void {
    this.employeeService.getEmployeeDetails(id).subscribe(
      response => {
        console.log('Employee details:', response);
        // Use the employee details as needed
      },
      error => {
        console.log('Error:', error);
      }
    );
  }

  updateEmployee(id: number, employee: any): void {
    this.employeeService.updateEmployee(id, employee).subscribe(
      response => {
        console.log('Employee updated:', response);
        // Refresh the employee list or perform any other necessary actions
      },
      error => {
        console.log('Error:', error);
      }
    );
  }
  deleteEmployee(id: number): void {
    if (confirm('Are you sure you want to delete this employee?')) {
      this.employeeService.deleteEmployee(id).subscribe(
        response => {
          console.log('Employee deleted:', response);
          // Refresh the employee list or perform any other necessary actions
        },
        error => {
          console.log('Error:', error);
        }
      );
    }
  }
  applyFilter() {
    const filterValue = this.searchValue.trim().toLowerCase();
    this.dataSource.filter = filterValue;
  }

}