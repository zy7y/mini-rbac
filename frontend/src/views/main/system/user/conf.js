// 表格数据列 表头配置
export const columns = [
  {
    title: "序号",
    dataIndex: "index",
    key: "index",
    align: "center",
    customRender: ({ text, record, index }) => `${index + 1}`,
  },
  {
    title: "用户名",
    dataIndex: "username",
    key: "username",
  },
  {
    title: "昵称",
    dataIndex: "nickname",
    key: "nickname",
  },
  {
    title: "状态",
    dataIndex: "status",
    key: "status",
  },
  {
    title: "创建时间",
    dataIndex: "created",
    key: "created",
  },
  {
    title: "更新时间",
    dataIndex: "modified",
    key: "modified",
  },
  {
    title: "操作",
    key: "action",
  },
];
