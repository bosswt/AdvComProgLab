import { StudentProvider } from "./../../providers/student/student";
import { Student } from "./../../models/student.model";
import { Component } from "@angular/core";
import { NavController } from "ionic-angular";
import { Observable } from "rxjs";

@Component({
  selector: "page-home",
  templateUrl: "home.html",
})
export class HomePage {
  public student: Observable<Student>;
  constructor(
    private studentProvider: StudentProvider,
    public navCtrl: NavController
  ) {}
  showScore(id: string) {
    this.student = this.studentProvider.getScore(id);
  }
}
