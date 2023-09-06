import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { InstructorService } from 'src/app/instructor.service';
import { UserService } from 'src/app/user.service';


@Component({
    selector: 'app-instructor-login',
    templateUrl: './instructor-login.component.html',
    styleUrls: ['./instructor-login.component.css']
})
export class InstructorLoginComponent {
    loginForm: FormGroup;
    signupForm: FormGroup;
    isSignup: boolean = false; // Initially, show the login form

    constructor(private userService: UserService,private fb: FormBuilder, private instructorService: InstructorService, private router: Router) {
        this.loginForm = this.fb.group({
            email: ['', [Validators.required, Validators.email]],
            password: ['', Validators.required]
        });

        this.signupForm = this.fb.group({
            name: ['', Validators.required],
            gender: ['', Validators.required],
            date_of_birth: ['', Validators.required],
            department: ['', Validators.required],
            email_signup: ['', [Validators.required, Validators.email]],
            contact_number: ['', Validators.required],
            password_signup: ['', Validators.required]
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
            const email = this.loginForm.get('email')!.value;
            const password = this.loginForm.get('password')!.value;

            // Call the InstructorService login method
            this.instructorService.loginInstructor(email, password).subscribe(
                res => {
                alert(res.message)
                if(res.response){
                    localStorage.setItem("loggedUserRole","instructor")
                    localStorage.setItem("user",JSON.stringify(res.user))
                        localStorage.setItem("token",JSON.stringify(res.token))
                    this.router.navigate(['/instructor-dashboard'])
                }

                },
                err => console.log(err)
            );
        }
    }

    onSignup() {
        if (this.signupForm.valid) {
            const name = this.signupForm.get('name')!.value;
            const gender = this.signupForm.get('gender')!.value;
            const dateOfBirth = this.signupForm.get('date_of_birth')!.value;
            const department = this.signupForm.get('department')!.value;
            const email = this.signupForm.get('email_signup')!.value;
            const contactNumber = this.signupForm.get('contact_number')!.value;
            const password = this.signupForm.get('password_signup')!.value;

            // Call the InstructorService signup method
            this.instructorService.signupInstructor({
                name,
                gender,
                date_of_birth: dateOfBirth,
                department,
                email,
                contact_number: contactNumber,
                password
            }).subscribe(
                res=>{
                    console.log(res)
                    alert(res.message)
                    
                    if(res.response){
                        
                        let currentUrl = this.router.url;
                        
                        this.router.navigateByUrl('/', {skipLocationChange: true}).then(() => {
                        this.router.navigate([currentUrl]);
                    });
                    }

                    },
                err => console.log(err)
            );
        }
    }
}
