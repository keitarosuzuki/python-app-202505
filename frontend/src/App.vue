<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

export default {
  data() {
    return {
      tasks: [],
      naturalInput: "",
      taskCount: "1",
    };
  },
  methods: {
    deleteTask(id) {
      fetch(`http://localhost:5000/api/tasks/${id}`, {
        method: "DELETE",
      })
        .then((res) => {
          if (res.ok) {
            this.tasks = this.tasks.filter((task) => task.id !== id);
          }
        });
    },
    generateTasks() {
      if (!this.naturalInput.trim()) return;

      fetch("http://localhost:5000/api/generate-tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
          {
            text: this.naturalInput,
            count: this.taskCount,
          }
        ),
      })
        .then((res) => res.json())
        .then((generatedTasks) => {
          this.tasks = []
          this.tasks = [...this.tasks, ...generatedTasks];
          this.naturalInput = "";
        })
        .catch((err) => {
          console.error("生成エラー:", err);
        });
    },
  },
}
</script>

<template>
  <div class="form-wrapper">
    <div class="task-section">
      <div class="form-floating">
        <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"
          v-model="naturalInput"></textarea>
        <label for="floatingTextarea2">やりたいこと</label>
      </div>
      <div class="generate-block">
        <div class="input-group">
          <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon"
            v-model="taskCount">
            <option value="1">1件</option>
            <option value="2">2件</option>
            <option value="3">3件</option>
            <option value="4">4件</option>
            <option value="5">5件</option>
          </select>
          <button class="btn btn-primary" type="button" @click="generateTasks">生成</button>
        </div>
      </div>
    </div>
    <div>
      <!-- <div>
        <div class="spinner-border text-primary" role="status"></div>
      </div> -->
      <div>
        <div class="card card-spacing" v-for="task in tasks" :key="task.id">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" />
                <label class="form-check-label" for="flexCheckChecked">
                  {{ task.text }}
                </label>
              </div>
              <div>
                <button type="button" class="btn-close" aria-label="Close" @click="deleteTask(task.id)"></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
