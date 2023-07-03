import { Component,Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup,FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { EmpdataserviceService } from '../empdataservice.service';
import {FloatLabelType, MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material/input';
import {MatRadioModule} from '@angular/material/radio';
import {MatCheckboxModule} from '@angular/material/checkbox';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.scss']
})
export class PopupComponent implements OnInit {
  form!: FormGroup;
  description!: string;
  
  constructor(@Inject(MAT_DIALOG_DATA) public data:any,private ref:MatDialogRef<PopupComponent>, private fb: FormBuilder, private service:EmpdataserviceService){}

  ngOnInit(): void {
    this.inputdata=this.data;

  }
  
  inputdata:any;
  
  closepopup()
  {
    this.ref.close('Closed using Function')
  }
  save() {
    this.ref.close(this.emp_add.value);
}
emp_add = this.fb.group({
  name:this.fb.control(''),
  address:this.fb.control(''),

})
Save_employee()
{
  console.log(this.emp_add.value);
  this.service.addEmployee(this.emp_add.value).subscribe(res=>{
  this.closepopup()
  });
}
}
