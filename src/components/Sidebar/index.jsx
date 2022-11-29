import React, { useState } from 'react'
import { SidebarData } from './SidebarData'
import * as FaIcons from 'react-icons/fa'
import { useDispatch } from 'react-redux'
import { startLogout } from '../../actions/auth'
import { Navbar, Nav, Button } from 'react-bootstrap'
import LogoSpread from '../Logo'
import AvatarVertical from '../Avatar' 
import './styles/sidebar.css'

function Sidebar() {
    function goTo() {
        window.location.reload(false);
    }
    const navLinkStyles = ({ isActive }) => {
        return {
            fontWeight: isActive ? 'bold' : 'normal',
            backgroundColor: isActive ? 'rgba(255, 255, 255, 0.500)' : '',
            color: isActive ? 'white' : ''
        }
    }

    const [sidebar, setSidebar] = useState(true)
    const dispatch = useDispatch()
    // const showSidebar = () => setSidebar(!sidebar)
    return (
        <Navbar collapseOnSelect expand='lg' className={sidebar ? 'navbar-expand-lg navbar-custom sidebar-sticky' : 'navbar-expand-lg navbar-custom'} >
            <Navbar.Brand as='div'>
                <LogoSpread/>
                <Navbar.Toggle className='hidden-lg-up float-xs-right' aria-controls='navbarScroll' />
            </Navbar.Brand>
            <Navbar.Collapse id='navbarScroll'>
                <AvatarVertical />
                <div className='scrolly'>
                    <Nav as='ul' navbarScroll>
                        {
                            SidebarData.map((item, index) =>{
                                return (
                                    <Nav.Item as='li' key={index} className='custom-nav-item'>
                                        <Nav.Link eventKey={index} href={item.path} onClick={() => window.location.reload(false)}  className={`${item.class} justify-content-start d-flex flex-row`}>
                                            {item.icon}
                                            <span>{item.title}</span>
                                        </Nav.Link>
                                    </Nav.Item>
                                )
                            })
                        }
                    </Nav>
                </div>
                <Nav as='ul' className='mb-0 logout'>
                    <Nav.Item as='li' className='custom-nav-item '>
                        <Nav.Link className='justify-content-center d-flex flex-row' onClick={() => dispatch(startLogout())}>
                            <FaIcons.FaSignOutAlt style={{fontSize: '16px'}} />
                            <span>Cerrar Sesión </span>
                        </Nav.Link>
                    </Nav.Item>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default Sidebar