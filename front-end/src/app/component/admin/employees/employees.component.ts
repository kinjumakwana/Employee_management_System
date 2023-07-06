import { AfterViewInit, Component, ViewChild,  EventEmitter, Output} from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTable, MatTableDataSource, MatTableModule} from '@angular/material/table';
import {MatSort, Sort, MatSortModule} from '@angular/material/sort';
import { Subject } from 'rxjs';
import { EmpdataserviceService } from '../employees/empdataservice.service'
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { HttpClient } from '@angular/common/http';
import { NgForm, NgModel } from '@angular/forms';
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

  constructor(private employeeService: EmpdataserviceService,
    private _liveAnnouncer: LiveAnnouncer, 
    private httClient:HttpClient,
    private modelService:NgbModal,private dialog:MatDialog) { 
    this.loademployee();
  }

  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  
  loademployee(){
      console.log("Call Load function")
      this.employeeService.getEmployees().subscribe(res=>{
      this.emp_data = res;
      this.dataSource = new MatTableDataSource<any>(this.emp_data.data);
      this.dataSource.data = this.emp_data.filteredData;
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
        ['username', 'first_name', 'last_name', 'email','gender', 'mobile_no', 'designation', 'department', 'address', 'date_of_birth', 'education', 'profile_pic', 'document', 'edit', 'delete'].includes(column.toLowerCase())
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

  // addEmployee(employee: any): void {
  //   this.employeeService.addEmployee(employee).subscribe(
  //     response => {
  //       console.log('New employee added:', response);
  //       // Refresh the employee list or perform any other necessary actions
  //       this.getEmployees(); // Refresh the employee list after adding a new employee
  //       this.refreshTable();
        
  //     },
  //     error => {
  //       console.log('Error:', error);
  //     }
  //   );
  // }

  addemployee(){
    this.Openpopup(0, 'Add Employee')
  }
  refreshTable(): void {
    this.employeeService.getEmployees().subscribe(
      response => {
        this.dataSource.data = response.data;
        this.dataSource._updateChangeSubscription();
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
        this.dataSource = new MatTableDataSource<any>(this.emp_data.filteredData);
        this.dataSource.filter = '';
        this.dataSource.connect();
        
      },
      error => {
        console.log('Error:', error);
      }
    );
  }

  updateEmp(id:number)
  { 
    console.log(id)
    this.Openpopup(id,'Edit Employee')
  }
  updateEmployee(id: number, employee: any): void {
    console.log(id)
    console.log(employee)
    this.employeeService.updateEmployee1(id, employee).subscribe(
      response => {
        console.log('Employee updated:', response);
        // Refresh the employee list or perform any other necessary actions
        this.getEmployees(); // Refresh the employee list after adding a new employee
        this.refreshTable();
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
          this.loademployee();
          this.refreshTable();

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
  Openpopup(id:any,title:any)
  {

    var _popup = this.dialog.open(PopupComponent,{
      width:'60%',
      enterAnimationDuration: '1000ms',
      exitAnimationDuration:'1000ms',
      data:{
        title:title,
        id:id,
      },
      
      
    })
    _popup.afterClosed().subscribe(item=>{
      console.log(item)
      this.refreshTable()
    })
  }

}