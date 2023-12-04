import React, { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        //
        const response = await fetch("http://localhost:8000/api/person/");
        if (!response.ok) {
          throw new Error("something went wrong");
        }
        const resData = await response.json();
        setUsers(resData);
      } catch (error) {
        setError(error);
      }
      setLoading(false);
    }
    fetchData();
  }, []);
  return (
    <>
      {error && <p>something went wrong !!</p>}
      {loading && <p>loading...</p>}
      {!error &&
        !loading &&
        users.map((user) => {
          return <li key={user.id}>{user.name}</li>;
        })}
    </>
  );
}

export default App;
