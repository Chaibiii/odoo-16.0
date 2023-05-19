/**@odoo-module **/

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart } = owl;
import { useService } from '@web/core/utils/hooks';

export class OwlTodoList extends Component {

        setup(){
            this.state = useState({

                task:{name:"", color:"#6495ED", completed:false},
                taskList:[],
                isEdit:false,
                activeId:false,

            })

            this.orm = useService("orm")
            this.model = "owl.todo.list"

            onWillStart(async ()=>{
                await getAllTasks();
            })
        }

        async getAllTasks(){
                this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "completed"])
            }


            addTask(){

            }

            editTask(){

            }

            async saveTask(){

            }


}
OwlTodoList.template = 'owl_new.TodoList'
registry.category('actions').add('owl_new.action_owl_todo_list_js', OwlTodoList);
