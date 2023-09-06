// import { StudentService } from './../../student.service';
import { StudentService } from 'src/app/student.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'app-student-login',
  templateUrl: './student-login.component.html',
  styleUrls: ['./student-login.component.css']
})
export class StudentLoginComponent implements OnInit{
  isSignup = false;
  loginForm!: FormGroup;
  signupForm!: FormGroup;

  constructor(private userService: UserService, private formBuilder: FormBuilder,   private http: HttpClient, private studentService:StudentService, private router: Router) {}
  ngOnInit(): void {
      this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]]
    });

    this.signupForm = this.formBuilder.group({
      name: ['', [Validators.required]],
      gender: ['', [Validators.required]],
      date_of_birth: ['', [Validators.required]],
      major: ['', [Validators.required]],
      email_signup: ['', [Validators.required, Validators.email]],
      contact_number: ['', [Validators.required]],
      password_signup: ['', [Validators.required, Validators.minLength(6)]]
    });
  }

  switchToLogin() {
    this.isSignup = false;
  }

  switchToSignup() {
    this.isSignup = true;
  }

  onLogin() {
    if (this.loginForm.valid) {
      // Handle login logic here
      const email = this.loginForm.get('email')!.value;
      const password = this.loginForm.get('password')!.value;
      // Perform login action with email and password
      
      this.studentService.loginStudent(email,password).subscribe(
        res => {
          alert(res.message)
          if(res.response){
            // this.userService.setUserRole("student")
            localStorage.setItem("loggedUserRole","student")

            this.router.navigate(['/student-dashboard'])
          }

        },
        err => console.log(err)
      )
    }
  }

  onSignup() {
    if (this.signupForm.valid) {
      // Handle signup logic here
      const newStudent = {
      name :this.signupForm.get('name')!.value,
      gender : this.signupForm.get('gender')!.value,
      date_of_birth : this.signupForm.get('date_of_birth')!.value,
      major : this.signupForm.get('major')!.value,
      email : this.signupForm.get('email_signup')!.value,
      contactNumber : this.signupForm.get('contact_number')!.value,
      password : this.signupForm.get('password_signup')!.value,
      }
     
      // Perform signup action with the form values


      this.studentService.signupStudent(newStudent).subscribe(
        res=>{
          console.log(res)
          alert(res.message)
          
          if(res.response){
            
            localStorage.setItem("user",JSON.stringify(res.user))
            
            let currentUrl = this.router.url;
            
            this.router.navigateByUrl('/', {skipLocationChange: true}).then(() => {
            this.router.navigate([currentUrl]);
          });
          }

        },
        err => console.log(err)
      )
    }
  }
}
