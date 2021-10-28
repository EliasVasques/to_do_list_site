function confirmExclusao(id) {
   if (confirm("Tem certeza que deseja excluir essa categoria?")) {
      location.href="delete_task/" + id;
   }
}
