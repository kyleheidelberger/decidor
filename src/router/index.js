import Vue from 'vue'
import Router from 'vue-router'
import ChoiceLogic from '@/components/ChoiceLogic'
import Decks from '@/components/Decks'
import Landing from '@/components/Landing'

Vue.use(Router)

export default new Router({
    routes: [
       {
        path: '/choicelogic',
        name:'ChoiceLogic',
        component: ChoiceLogic
       },
       {
        path: '/decks',
        name:'Decks',
        component: Decks
        },
        {
        path: '/landing',
        name:'Landing',
        component: Landing
        },
    ]
})
