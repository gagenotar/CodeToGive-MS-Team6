// Form.jsx
import React from 'react';

function Form({ fields, onSubmit, buttonText }) {
    return (
        <form onSubmit={onSubmit}>
            {fields.map((field, index) => (
                <div key={index}>
                    <label>{field.label}</label>
                    <input
                        type={field.type}
                        name={field.name}
                        value={field.value}
                        onChange={field.onChange}
                    />
                </div>
            ))}
            <button type="submit">{buttonText}</button>
        </form>
    );
}

export default Form;