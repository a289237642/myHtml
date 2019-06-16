import React, {Component} from 'react'
import {
    Card,
    Table,
    Button,
    Icon,
    message
} from 'antd'
import LinkButton from "../../components/link-button";
import {reqCategorys} from '../../api'
/*
Category
 */
export default class Category extends Component {
    state = {
        loading: false,// 是否正在获取数据中
        categorys: [],//一级分类列表
        subCategorys: [], // 二级分类列表
        parentId: '0', // 当前需要显示的分类列表的父分类ID
    }

    //初始化Table所有列的数组
    initColumns = () => {
        this.columns = [
            {
                title: '分类的名称',
                dataIndex: 'name',
            },
            {
                title: '操作',
                width: 300,
                render: () => (
                    <span>
                        <LinkButton>修改分类</LinkButton>
                        <LinkButton>查看子分类</LinkButton>
                    </span>
                )
            }
        ]
    }

    //异步获取一级分类
    getCategorys = async () => {

        this.setState({
            loading:true
        })

        // 发异步ajax请求, 获取数据
        const result = await reqCategorys('0')
        this.setState({
            loading:false
        })
        // 在请求完成后, 隐藏loading
        this.setState({loading: false})

        if (result.status === 0) {
            // 取出分类数组(可能是一级也可能二级的)
            const categorys = result.data
            // 更新一级分类状态
            this.setState({
                categorys
            })
        } else {
            message.error('获取分类列表失败')
        }
    }


    //   为第一次render()准备数据
    componentWillMount() {
        this.initColumns()
    }

    //执行异步任务，发送ajax请求
    componentDidMount() {
        this.getCategorys()
    }


    render() {
        const {categorys,loading} = this.state
        const title = "一级分类列表"
        const extra = (
            <Button type='primary'>
                <Icon type='plus'/>
                添加
            </Button>
        )

        return (
            <Card title={title} extra={extra}>
                <Table
                    bordered
                    rowKey='_id'
                    loading={loading}
                    dataSource={categorys}
                    columns={this.columns}
                    pagination={{defaultPageSize: 5, showQuickJumper: true}}
                />

            </Card>
        )
    }
}

