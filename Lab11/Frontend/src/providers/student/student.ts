import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import "rxjs/add/operator/map";

/*
  Generated class for the StudentProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class StudentProvider {
  constructor(public http: HttpClient) {}
  getScore(studentList: Array<object>, id: number, event: any) {
    this.http
      .get("http://c76723a87d96.ngrok.io/getscore?id=" + id)
      .subscribe((data) => {
        data.data.forEach((student) => studentList.push(student));
        if (id != 0) event.complete();
      });
  }
}
