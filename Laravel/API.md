### GET /api/students 
    - retornará todos os alunos e aceitará solicitações GET.
### GET /api/students/{id} 
    - retornará um registro de aluno fazendo referência a seu id e aceitando solicitações GET.
### POST /api/students 
    - criará um novo registro de alunos e aceitará solicitações POST.
### PUT /api/students/{id}
    - atualizará um registro existente de aluno fazendo referência a seu id e aceitando solicitações PUT.
### DELETE /api/students/{id} 
    - excluirá um registro de aluno fazendo referência a seu id e aceitando solicitações DELETE.
### Criando Model Student
    - php artisan make:model Student 
#### App\Models\Student.php
```php
class Student extends Model
{
    protected $table = 'students';

    protected $fillable = ['name', 'course'];
}
```
### Criando o Controller
    - php artisan make:controller ApiController
```php
<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Student;
class ApiController extends Controller
{
  public function getAllStudents() {
    if(Student::get()->count()){
      $students = Student::All();
      return response()->json($students,200);
    }else{
      return response()->json(['Mensagem'=>'Não existe resultado para sua Pesquisa'],400);
    }
  }

  public function createStudent(Request $request) {
      $student = new Student;
      $student->name = $request->name;
      $student->course = $request->course;
      $student->save();
      return response()->json(["message" => "Estudante Cadastrado com Sucesso"], 201);
  }
  
  public function getStudent($id) {
    if (Student::where('id', $id)->exists()) {
      $student = Student::where('id', $id)->get();
      return response()->json($student,200);
    }else{
      return response()->json(["message" => "Estudante não encontrado."], 404);
    }
  }
  
  public function updateStudent(Request $request, $id) {
    if (Student::where('id', $id)->exists()) {
      $student = Student::find($id);
      $student->name = is_null($request->name) ? $student->name : $request->name;
      $student->course = is_null($request->course) ? $student->course : $request->course;
      $student->save();
      return response()->json(["message" => "records updated successfully"], 200);
    }else{
      return response()->json(["message" => "Não encontrado"], 404);
    }
  }
  
  public function deleteStudent ($id) {
    if(Student::where('id', $id)->exists()) {
      $student = Student::find($id);
      $student->delete();
      return response()->json(["message" => "records deleted"], 202);
    }else{
      return response()->json(["message" => "Student not found"], 404);
    }
  }
}
```
#### routes/api.php
```php
use  App\Http\Controllers\ApiController;
Route::get('students', [ApiController::class,'getAllStudents']);
Route::get('students/{id}', [ApiController::class,'getStudent']);
Route::post('students',[ApiController::class,'createStudent']);
Route::put('students/{id}',[ApiController::class,'updateStudent']);
Route::delete('students/{id}',[ApiController::class,'deleteStudent']);
```
