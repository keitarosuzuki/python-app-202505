<script setup>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
</script>

<template>
  <div class="form-wrapper">
    <div class="task-section">
      <div class="form-floating">
        <textarea
          class="form-control"
          placeholder="Leave a comment here"
          id="floatingTextarea2"
          style="height: 100px"
        ></textarea>
        <label for="floatingTextarea2">やりたいこと</label>
      </div>
      <div class="generate-block">
        <div class="input-group">
          <select
            class="form-select"
            id="inputGroupSelect04"
            aria-label="Example select with button addon"
          >
            <option value="1" selected>1件</option>
            <option value="2">2件</option>
            <option value="3">3件</option>
            <option value="4">4件</option>
            <option value="5">5件</option>
          </select>
          <button class="btn btn-primary" type="button">生成</button>
        </div>
      </div>
    </div>
    <div>
      <!-- <div>
        <div class="spinner-border text-primary" role="status"></div>
      </div> -->
      <div>
        <div class="card card-spacing">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="flexCheckChecked"
                />
                <label class="form-check-label" for="flexCheckChecked">
                  生成されたタスク
                </label>
              </div>
              <div>
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
        <div class="card card-spacing">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="flexCheckChecked"
                />
                <label class="form-check-label" for="flexCheckChecked">
                  生成されたタスク
                </label>
              </div>
              <div>
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
        <div class="card card-spacing">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="flexCheckChecked"
                />
                <label class="form-check-label" for="flexCheckChecked">
                  生成されたタスク
                </label>
              </div>
              <div>
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
        <div class="card card-spacing">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="flexCheckChecked"
                />
                <label class="form-check-label" for="flexCheckChecked">
                  生成されたタスク
                </label>
              </div>
              <div>
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
        <div class="card card-spacing">
          <div class="card-body">
            <div class="card-inner">
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  value=""
                  id="flexCheckChecked"
                  checked
                />
                <label
                  class="form-check-label text-decoration-line-through"
                  for="flexCheckChecked"
                >
                  生成されたタスク
                </label>
              </div>
              <div>
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                ></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
