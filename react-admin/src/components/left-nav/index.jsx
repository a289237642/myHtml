import React, {Component} from 'react'
import {Link} from 'react-router-dom'
import {Menu, Icon} from 'antd'

import './index.less'
import logo from '../../assets/images/logo.png'
import menuList from '../../config/menuConfig'

const SubMenu = Menu.SubMenu

export default class Index extends Component {

    getMenuNodes_map = (menuList) => {
        return menuList.map(item => {
            if (!item.children) {
                return (
                    <Menu.Item key={item.key}>
                        <Link to={item.key}>
                            <Icon type={item.icon}/>
                            <span>{item.title}</span>
                        </Link>
                    </Menu.Item>
                )
            } else {
                return (
                    <SubMenu
                        key={item.key}
                        title={
                            <span>
                    <Icon type={item.icon}/>
                    <span> {item.title}</span>
                    </span>
                        }>
                        {this.getMenuNodes(item.children)}
                    </SubMenu>
                )
            }
        })
    }

    getMenuNodes = (menuList) => {
        return menuList.reduce((pre, item) => {
            if (!item.children) {
                pre.push((
                    <Menu.Item key={item.key}>
                        <Link to={item.key}>
                            <Icon type={item.icon}/>
                            <span>{item.title}</span>
                        </Link>
                    </Menu.Item>
                ))
            } else {
                pre.push((
                    <SubMenu
                        key={item.key}
                        title={
                            <span>
                    <Icon type={item.icon}/>
                    <span> {item.title}</span>
                    </span>
                        }>
                        {this.getMenuNodes(item.children)}
                    </SubMenu>
                ))

            }
            return pre
        }, [])

    }

    render() {
        return (
            <div className="left-nav">
                <Link to='/' className="left-nav-header">
                    <img src={logo} alt="logo"/>
                    <h1>硅谷后台</h1>
                </Link>

                <Menu mode="inline" theme="dark">
                    {
                        this.getMenuNodes(menuList)
                    }
                </Menu>
            </div>
        )
    }
}
