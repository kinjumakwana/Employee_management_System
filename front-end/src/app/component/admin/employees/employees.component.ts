import { AfterViewInit, Component, ViewChild,  EventEmitter, Output} from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatSort, Sort, MatSortModule} from '@angular/material/sort';
import { Subject } from 'rxjs';
import { EmpdataserviceService } from '../employees/empdataservice.service'
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { HttpClient } from '@angular/common/http';
import { NgModel } from '@angular/forms';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import {MatDialog, MatDialogConfig, MatDialogModule} from '@angular/material/dialog';
import { PopupComponent } from './popup/popup.component';
import {MatDatepickerModule} from '@angular/material/datepicker';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.scss']
})

export class EmployeesComponent{
  employees: any[] = [];
  displayedColumns: string[] = [];
  displayuser:string[]=[];
  newEmployee: any = {};
  emp_data  = new  MatTableDataSource<any>([]);
  dataSource = new MatTableDataSource<any>([]);
  searchValue!: string;
  closeResult!:string;


  constructor(private employeeService: EmpdataserviceService,private _liveAnnouncer: LiveAnnouncer, private httClient:HttpClient,private modelService:NgbModal,private dialog:MatDialog) { 
   this.loademployee();
  }


  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  loademployee(){
      this.employeeService.getEmployees().subscribe(res=>{
      this.emp_data = res;
      // this.dataSource =  new MatTableDataSource<Customer>(this.emp_data);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
      });
  }
 
  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }
  ngOnInit(): void {
    this.dataSource = new MatTableDataSource<any>();
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
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
          // Get the keys of the first object in filteredData
        const keys = Object.keys(this.emp_data.filteredData[0]);
        let modifiedUserKeys: string[] = [];

        // Check if 'user' field exists and extract its keys
        if (keys.includes('user')) {
        //   modifiedUserKeys = Object.keys(this.emp_data.filteredData[0].user)
        //     .map(key => key === 'id' ? 'User_id' : key);
        //   console.log(modifiedUserKeys);

        //   // Remove 'user' from the displayedColumns array
        //   this.displayedColumns = this.displayedColumns.filter(column => column !== 'user');
        // }

        // // Update displayedColumns with modifiedUserKeys and keys
        // this.displayedColumns = [...modifiedUserKeys, ...keys];
        // console.log(this.displayedColumns);
        // } else {
        //   this.displayedColumns = ['Id', 'Gender', 'Mobile_no', 'Designation', 'Department', 'Address', 'Date_of_birth', 'Education', 'Profile_pic', 'Document', 'created_at', 'User', 'Action'];
        // }
          const userKeys = Object.keys(this.emp_data.filteredData[0].user);
          console.log(userKeys)
            
          // Replace 'id' with 'user_id' in userKeys array
          const modifiedUserKeys = userKeys.map(key => key === 'id' ? 'user_id' : key);
          console.log(modifiedUserKeys);
  
          // Add the user field keys to displayedColumns
          this.displayedColumns = [...modifiedUserKeys,...keys];
          this.displayuser = userKeys
        }
         else {
          this.displayedColumns = keys
        
        }
      
      // Filter out the unwanted keys from displayedColumns
      this.displayedColumns = this.displayedColumns.filter(column =>
        ['username', 'first_name', 'last_name', 'email', 'gender', 'mobile_no', 'designation', 'department', 'address', 'date_of_birth', 'education', 'profile_pic', 'document', 'edit', 'delete'].includes(column.toLowerCase())
      );
        
      console.log(this.displayedColumns);
      } 
    else {
      this.displayedColumns = ['username', 'first_name', 'last_name', 'email', 'gender', 'mobile_no', 'designation', 'department', 'address', 'date_of_birth', 'education', 'profile_pic', 'document', 'created_at', 'edit', 'delete'];
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
        this.dataSource.data.push(response);
        this.dataSource._updateChangeSubscription();
        this.newEmployee = {};
        this.loademployee();
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
    console.log(filterValue)
  }
  refreshPage() {
    window.location.reload();
  }
  Openpopup()
  {

    var _popup = this.dialog.open(PopupComponent,{
      width:'60%',
      enterAnimationDuration: '1000ms',
      exitAnimationDuration:'1000ms',
      data:{
        title:'Add Employee'
      },
      
      
    })
    _popup.afterClosed().subscribe(item=>{
      console.log(item)
      this.loademployee()
    })
  }

}