
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

const StudentPublicProfile = ({ student }) => {
      const background_color = "#e33940";
      const hover_color = "#820000";
  return (
    <>
          <style type="text/css">
        {`
  .btn-red {
    color: #fff;
    background-color: ${background_color};
    border-color: ${background_color};

  }

  .btn-red:hover{
    color: #fff;
    background-color: ${hover_color};
  }


  }
    `}
      </style>
    <Card.Body>
      <Card.Title>Profile</Card.Title>
      <Card.Text>{student.student_name}</Card.Text>
      <Card.Text>{student.email}</Card.Text>
      <Card.Text>{student.experience}</Card.Text>
      <Card.Text>{student.major}</Card.Text>
      <Button variant="red" className="btn-bd-primary" href="/profile">
        View Profile
      </Button>
    </Card.Body>
    </>
  );
};

export default StudentPublicProfile;