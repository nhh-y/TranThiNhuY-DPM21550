import React from "react";
import { Link } from "react-router-dom";

const Dashboard = () => {
    return (
        <div className="container">
            <h2>Quản lý Đề kiểm tra</h2>
            <Link to="/create-quiz">Tạo đề kiểm tra</Link>
        </div>
    );
};

export default Dashboard;
