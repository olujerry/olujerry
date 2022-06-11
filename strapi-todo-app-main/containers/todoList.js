import TodoItem from "../components/todoItem";

function TodoList({ todos, editTodoItem, deleteTodoItem }) {
  return (
    <div className="todoListContainer">
      <div className="todosText">Todos</div>
      {todos
        .sort((a, b) => b.created_at.localeCompare(a.created_at))
        .map((todo, i) => (
          <TodoItem
            todo={todo}
            key={i}
            deleteTodoItem={deleteTodoItem}
            editTodoItem={editTodoItem}
          />
        ))}
    </div>
  );
}

export default TodoList;
