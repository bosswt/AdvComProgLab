import { StudentProvider } from "./../../providers/student/student";
import { Component } from "@angular/core";
import { NavController } from "ionic-angular";

@Component({
  selector: "page-home",
  templateUrl: "home.html",
})
export class HomePage {
  studentList = [];
  pageNumber = 0;
  constructor(
    public navCtrl: NavController,
    public studentProvider: StudentProvider
  ) {}
  ionViewDidLoad() {
    this.studentProvider.getScore(this.studentList, 0, "");
    console.log(this.studentList);
  }
  doInfinite(event) {
    this.pageNumber++;
    if (this.pageNumber * 20 == 1020) event.enable(false);
    else {
      this.studentProvider.getScore(
        this.studentList,
        this.pageNumber * 20,
        event
      );
    }
  }
}
