import React from 'react';
import * as FaIcons from 'react-icons/fa'

export const SidebarData = [
    {
        title: 'Dashboard',
        path: '/dashboard',
        icon: <FaIcons.FaChartLine />,
        class: 'disabled'
    },
    {
        title: 'Primera Milla',
        path: '/firstmile',
        icon: <FaIcons.FaBoxOpen />,
        class: 'disabled'
    },
    {
        title: 'Planificación',
        path: '/planning',
        icon: <FaIcons.FaMapMarkedAlt />,
        class: ''
    },
    {
        title: 'Sorting',
        path: '/sorting',
        icon: <FaIcons.FaClipboardList />,
        class: 'disabled'
    },
    {
        title: 'Despacho',
        path: '/dispatch',
        icon: <FaIcons.FaShippingFast />,
        class: 'disabled'
    },
    {
        title: 'Última Milla',
        path: '/lastmile',
        icon: <FaIcons.FaPeopleCarry />,
        class: 'disabled'
    },
    {
        title: 'Gestión Almacen',
        path: '/wms',
        icon: <FaIcons.FaSync />,
        class: 'disabled'
    },
    {
        title: 'Logística Inversa',
        path: '/reverse-logistic',
        icon: <FaIcons.FaUndoAlt />,
        class: 'disabled'
    },
    {
        title: 'Herramientas',
        path: '/tools',
        icon: <FaIcons.FaTools />,
        class: 'disabled'
    },
    {
        title: 'Búsqueda',
        path: '/search',
        icon: <FaIcons.FaSearch />,
        class: 'disabled'
    },

]
