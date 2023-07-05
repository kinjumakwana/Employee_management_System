import { Component,Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup,FormControl, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { EmpdataserviceService } from '../empdataservice.service';
import {FloatLabelType, MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material/input';
import {MatRadioModule} from '@angular/material/radio';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { formatDate } from '@angular/common';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.scss']
})
export class PopupComponent implements OnInit {
  // form!: FormGroup;
  description!: string;
  email = new FormControl('', [Validators.required, Validators.email]);
  hide = true;
  isEditMode: boolean = false;
  inputdata:any;
  editdata:any;
  emp_add!: FormGroup; // Rename 'form' to 'emp_add'
  constructor(
    @Inject(MAT_DIALOG_DATA) public data:any,
  private ref:MatDialogRef<PopupComponent>, 
  private fb: FormBuilder, 
  private service:EmpdataserviceService){}
  
  ngOnInit(): void {
    this.inputdata=this.data;
    if (this.inputdata.id>0){
      this.setpopupdata(this.inputdata.id)
    }

    this.emp_add = this.fb.group({
      username: ['', Validators.required],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      gender: ['', Validators.required],
      mobile_no: ['', Validators.required],
      designation: ['', Validators.required],
      department: ['', Validators.required],
      address: ['', Validators.required],
      date_of_birth: ['', Validators.required],
      education: ['', Validators.required],
      profile_pic: ['', Validators.required],
      document: ['', Validators.required],

    });

  }
  
  getErrorMessage() {
    if (this.email.hasError('required')) {
      return 'You must enter a value';
    }

    return this.email.hasError('email') ? 'Not a valid email' : '';
  }
  // ['username', 'first_name', 'last_name', 'email','password', 'gender', 'mobile_no', 'designation', 'department', 'address', 'date_of_birth', 'education', 'profile_pic', 'document', 'edit', 'delete']
  setpopupdata(id:any)
  {
    if (id) {
    this.isEditMode = true;
    this.service.getEmployeeDetails(id).subscribe(res=>{
      this.editdata = res;
      console.log(this.editdata)
      this.emp_add.setValue({
        username:this.editdata.user.username,
        first_name:this.editdata.user.first_name,
        last_name:this.editdata.user.last_name,
        email:this.editdata.user.email,
        password:this.editdata.user.password,
        gender:this.editdata.gender,
        mobile_no:this.editdata.mobile_no,
        designation:this.editdata.designation,
        department:this.editdata.department,
        address:this.editdata.address,
        date_of_birth:this.editdata.date_of_birth,
        education:this.editdata.education,
        profile_pic:this.editdata.profile_pic,
        document:this.editdata.document

      })
    })
    }else {
      this.isEditMode = false;
    }
    
  }

  closepopup()
  { 
   this.ref.close('Closed using Function')
  }

  onFormSubmit() {
    if (this.isEditMode) {
      this.update(); // Call the update method for edit mode
    } else {
      this.save(); // Call the save method for add mode
    }
  }

  save() 
  {
        this.ref.close(this.emp_add.value);
        if (this.emp_add.value.date_of_birth === '') {
          // Handle the case when the date of birth is empty
          console.log('Date of birth is required.');
          return;
          
        }
        // Format the date_of_birth value before sending it to the API
        const formattedDateOfBirth = formatDate(this.emp_add.value.date_of_birth, 'yyyy-MM-dd', 'en-US');
      
        // Update the date_of_birth value in the form group
        this.emp_add.patchValue({ date_of_birth: formattedDateOfBirth });
      
        const formData = new FormData();

        // Append form values
        Object.keys(this.emp_add.value).forEach(key => {
          if (key === 'profile_pic' || key === 'document' || key === 'date_of_birth' ) {
          // Append files separately
          formData.append(key, this.emp_add.value[key]);
        } else {
          formData.append(key, this.emp_add.value[key]);
        }
      });

      console.log(formData);

      console.log(this.emp_add.value);

      this.service.addEmployee(formData).subscribe(res=>{
      console.log('New employee added:', res);
      this.closepopup()


      });

  }
  update() {
    this.ref.close(this.emp_add.value);
    const id = this.editdata.id;
    if (this.emp_add.value.date_of_birth === '') {
      // Handle the case when the date of birth is empty
      console.log('Date of birth is required.');
      return;
      
    }
    // Format the date_of_birth value before sending it to the API
    const formattedDateOfBirth = formatDate(this.emp_add.value.date_of_birth, 'yyyy-MM-dd', 'en-US');
  
    // Update the date_of_birth value in the form group
    this.emp_add.patchValue({ date_of_birth: formattedDateOfBirth });
  
    const formData = new FormData();

    // Append form values
    Object.keys(this.emp_add.value).forEach(key => {
      if (key === 'profile_pic' || key === 'document' || key === 'date_of_birth' ) {
      // Append files separately
      formData.append(key, this.emp_add.value[key]);
    } else {
      formData.append(key, this.emp_add.value[key]);
    }
  });

  console.log(formData);

  console.log(this.emp_add.value);

  this.service.updateEmployee1(id,formData).subscribe(res=>{
  console.log('Updated employee:', res);
  this.closepopup()
  });

  }

onProfilePicSelected(event: any) {
  if (event.target.files && event.target.files.length > 0) {
    const file = event.target.files[0];
    console.log(file)
    this.emp_add.patchValue({ profile_pic: file });
  }
}

onDocumentSelected(event: any) {
  if (event.target.files && event.target.files.length > 0) {
    const file = event.target.files[0];
    console.log(file)
    this.emp_add.patchValue({ document: file });
  }
}

}
