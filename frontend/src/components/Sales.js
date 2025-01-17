import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const Sales = () => {
    const [sales, setSales] = useState([]);
    const [form, setForm] = useState({ product_id: '', qty: '', price: '', date: '' });

    useEffect(() => {
        fetchSales();
    }, []);

    const fetchSales = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/sales');
            setSales(response.data);
        } catch (error) {
            console.error('Error fetching sales:', error);
        }
    };

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:5000/sales', form);
            fetchSales();
        } catch (error) {
            console.error('Error adding sale:', error);
        }
    };

    return (
        <div className="container">
            <h1>Sales</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Product ID</label>
                    <input type="text" name="product_id" className="form-control" onChange={handleChange} />
                </div>
                <div className="form-group">
                    <label>Quantity</label>
                    <input type="text" name="qty" className="form-control" onChange={handleChange} />
                </div>
                <div className="form-group">
                    <label>Price</label>
                    <input type="text" name="price" className="form-control" onChange={handleChange} />
                </div>
                <div className="form-group">
                    <label>Date</label>
                    <input type="text" name="date" className="form-control" onChange={handleChange} />
                </div>
                <button type="submit" className="btn btn-primary">Add Sale</button>
            </form>
            <table className="table mt-4">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Product ID</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {sales.map(sale => (
                        <tr key={sale.id}>
                            <td>{sale.id}</td>
                            <td>{sale.product_id}</td>
                            <td>{sale.qty}</td>
                            <td>{sale.price}</td>
                            <td>{sale.date}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Sales;