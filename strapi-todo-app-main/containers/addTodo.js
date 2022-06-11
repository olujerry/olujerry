function AddTodo({ addTodo }) {
  return (
    <>
      <div className="addTodoContainer">
        <input
          className="todoInputText"
          type="text"
          placeholder="Add new todo here..."
          id="todoText"
          onKeyDown={(e) => {
            if (e.code === "Enter") {
              addTodo(todoText.value);
              todoText.value = "";
            }
          }}
        />
        <input
          className="todoInputButton"
          type="button"
          value="Add Todo"
          onClick={() => {
            addTodo(todoText.value);
            todoText.value = "";
          }}
        />
      </div>
    </>
  );
}

export default AddTodo;
