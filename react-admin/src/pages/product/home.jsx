import React, {Component} from 'react'
import {
    Card,
    Select,
    Input,
    Icon,
    Button,
    Table
} from 'antd'
import LinkButton from "../../components/link-button";
import {reqProducts, reqSearchProducts} from '../../api'
import {PAGE_SIZE} from '../../utils/constants'


const Option = Select.Option
/*
ProductHome
 */
export default class ProductHome extends Component {
    state = {
        total: 0,
        products: [],//商品数组
        loading: false,
        searchName: '',//搜索关键字
        searchType: ''//根据商品名称搜索

    }


    //初始化table列的数组
    initColumns = () => {
        this.columns = [
            {
                title: '商品名称',
                dataIndex: 'name',
            },
            {
                title: '商品描述',
                dataIndex: 'desc',
            },
            {
                title: '价格',
                dataIndex: 'price',
                render: (price) => '￥' + price
            },
            {
                width: 100,
                title: '状态',
                dataIndex: 'status',
                render: (status) => {
                    return (
                        <span>
                            <Button type='primary'>下架</Button>
                            <span>在售</span>
                        </span>
                    )
                }
            },
            {
                width: 100,
                title: '操作',
                render: (product) => {
                    return (
                        <span>
                             <LinkButton
                                 onClick={() => this.props.history.push('/product/detail', {product})}>详情</LinkButton>
                            <LinkButton
                                onClick={() => this.props.history.push('/product/addupdate', product)}>修改</LinkButton>
                        </span>
                    )
                }
            },
        ]
    }

    //获取指定页码的的列表显示
    getProducts = async (pageNum) => {
        this.setState({loading: true})
        const {searchName, searchType} = this.state
        let result
        if (searchType) {
            result = await reqSearchProducts({pageNum, pageSize: PAGE_SIZE, searchName, searchType})
        } else {
            result = await reqProducts(pageNum, PAGE_SIZE)
        }

        this.setState({loading: false})

        console.log(result)
        if (result.status === 0) {
            const {total, list} = result.data
            this.setState({
                total,
                products: list
            })

        }

    }

    componentWillMount() {
        this.initColumns()
    }

    componentDidMount() {
        this.getProducts(1)
    }

    render() {
        const {products, total, loading, searchName, searchType} = this.state


        const title = (
            <span>
            <Select value={searchType} style={{width: 150}}
                    onChange={value => this.setState({searchType: value})}>
                <Option value='productName'>按名称搜索</Option>
                <Option value='productDesc'>按描述搜索</Option>
            </Select>
            <Input placeholder='请输入关键字' style={{width: 150, margin: '0 15px'}}
                   value={searchName}
                   onChange={event => this.setState({searchName: event.target.value})}/>
            <Button type='primary' onClick={() => this.getProducts(1)}>搜索</Button>
        </span>
        )

        const extra = (
            <Button type='primary'>
                <Icon type='plus'/>添加商品
            </Button>
        )


        return (
            <Card title={title} extra={extra}>
                <Table
                    bordered
                    rowKey='_id'
                    loading={loading}
                    dataSource={products}
                    columns={this.columns}
                    pagination={{
                        total,
                        defaultPageSize: PAGE_SIZE,
                        showQuickJumper: true,
                        onChange: this.getProducts
                    }}
                />
            </Card>
        )
    }
}
